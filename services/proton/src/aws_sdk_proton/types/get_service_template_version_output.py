"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceTemplateVersionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_template_version


class GetServiceTemplateVersionOutput(TypedDict, closed=True):
    service_template_version: (
        "aws_sdk_proton.types.service_template_version.ServiceTemplateVersion"
    )
    """<p>The detailed data of the requested service template version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceTemplateVersionOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.service_template_version

    out["serviceTemplateVersion"] = (
        aws_sdk_proton.types.service_template_version.serialize_aws_json_1_0(
            value["service_template_version"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceTemplateVersionOutput:
    out: GetServiceTemplateVersionOutput = {}  # type: ignore[typeddict-item]
    if "serviceTemplateVersion" in data:
        import aws_sdk_proton.types.service_template_version

        out["service_template_version"] = (
            aws_sdk_proton.types.service_template_version.deserialize_aws_json_1_0(
                data["serviceTemplateVersion"]
            )
        )
    else:
        raise DeserializationError(
            "GetServiceTemplateVersionOutput.service_template_version required"
        )
    return out
