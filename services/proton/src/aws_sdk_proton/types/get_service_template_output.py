"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_template


class GetServiceTemplateOutput(TypedDict, closed=True):
    service_template: "aws_sdk_proton.types.service_template.ServiceTemplate"
    """<p>The detailed data of the requested service template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceTemplateOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.service_template

    out["serviceTemplate"] = (
        aws_sdk_proton.types.service_template.serialize_aws_json_1_0(
            value["service_template"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceTemplateOutput:
    out: GetServiceTemplateOutput = {}  # type: ignore[typeddict-item]
    if "serviceTemplate" in data:
        import aws_sdk_proton.types.service_template

        out["service_template"] = (
            aws_sdk_proton.types.service_template.deserialize_aws_json_1_0(
                data["serviceTemplate"]
            )
        )
    else:
        raise DeserializationError("GetServiceTemplateOutput.service_template required")
    return out
