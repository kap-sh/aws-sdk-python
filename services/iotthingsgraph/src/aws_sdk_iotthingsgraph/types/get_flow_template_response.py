"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetFlowTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.flow_template_description


class GetFlowTemplateResponse(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_iotthingsgraph.types.flow_template_description.FlowTemplateDescription"
    ]
    """<p>The object that describes the specified workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFlowTemplateResponse) -> dict:
    out: dict = {}
    if "description" in value:
        import aws_sdk_iotthingsgraph.types.flow_template_description

        out["description"] = (
            aws_sdk_iotthingsgraph.types.flow_template_description.serialize_aws_json_1_1(
                value["description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFlowTemplateResponse:
    out: GetFlowTemplateResponse = {}  # type: ignore[typeddict-item]
    if "description" in data:
        import aws_sdk_iotthingsgraph.types.flow_template_description

        out["description"] = (
            aws_sdk_iotthingsgraph.types.flow_template_description.deserialize_aws_json_1_1(
                data["description"]
            )
        )
    return out
