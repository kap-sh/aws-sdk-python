"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceTemplateVersionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.service_template_version


class UpdateServiceTemplateVersionOutput(TypedDict, closed=True):
    service_template_version: (
        "capo_proton.types.service_template_version.ServiceTemplateVersion"
    )
    """<p>The service template version detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceTemplateVersionOutput) -> dict:
    out: dict = {}
    import capo_proton.types.service_template_version

    out["serviceTemplateVersion"] = (
        capo_proton.types.service_template_version.serialize_aws_json_1_0(
            value["service_template_version"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceTemplateVersionOutput:
    out: UpdateServiceTemplateVersionOutput = {}  # type: ignore[typeddict-item]
    if "serviceTemplateVersion" in data:
        import capo_proton.types.service_template_version

        out["service_template_version"] = (
            capo_proton.types.service_template_version.deserialize_aws_json_1_0(
                data["serviceTemplateVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceTemplateVersionOutput.service_template_version required"
        )
    return out
