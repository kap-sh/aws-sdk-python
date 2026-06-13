"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceTemplateVersionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_template_version


class UpdateServiceTemplateVersionOutput(TypedDict):
    service_template_version: (
        "aws_sdk_proton.types.service_template_version.ServiceTemplateVersion"
    )
    """<p>The service template version detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceTemplateVersionOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.service_template_version

    out["serviceTemplateVersion"] = (
        aws_sdk_proton.types.service_template_version.serialize_aws_json_1_0(
            value["service_template_version"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceTemplateVersionOutput:
    out: UpdateServiceTemplateVersionOutput = {}  # type: ignore[typeddict-item]
    if "serviceTemplateVersion" in data:
        import aws_sdk_proton.types.service_template_version

        out["service_template_version"] = (
            aws_sdk_proton.types.service_template_version.deserialize_aws_json_1_0(
                data["serviceTemplateVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceTemplateVersionOutput.service_template_version required"
        )
    return out
