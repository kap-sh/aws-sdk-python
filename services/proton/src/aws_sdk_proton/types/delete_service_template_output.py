"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_template


class DeleteServiceTemplateOutput(TypedDict):
    service_template: NotRequired[
        "aws_sdk_proton.types.service_template.ServiceTemplate"
    ]
    """<p>The detailed data of the service template being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceTemplateOutput) -> dict:
    out: dict = {}
    if "service_template" in value:
        import aws_sdk_proton.types.service_template

        out["serviceTemplate"] = (
            aws_sdk_proton.types.service_template.serialize_aws_json_1_0(
                value["service_template"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceTemplateOutput:
    out: DeleteServiceTemplateOutput = {}  # type: ignore[typeddict-item]
    if "serviceTemplate" in data:
        import aws_sdk_proton.types.service_template

        out["service_template"] = (
            aws_sdk_proton.types.service_template.deserialize_aws_json_1_0(
                data["serviceTemplate"]
            )
        )
    return out
