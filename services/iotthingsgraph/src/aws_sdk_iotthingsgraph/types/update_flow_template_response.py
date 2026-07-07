"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UpdateFlowTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.flow_template_summary


class UpdateFlowTemplateResponse(TypedDict, closed=True):
    summary: NotRequired[
        "aws_sdk_iotthingsgraph.types.flow_template_summary.FlowTemplateSummary"
    ]
    """<p>An object containing summary information about the updated workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFlowTemplateResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import aws_sdk_iotthingsgraph.types.flow_template_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.flow_template_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFlowTemplateResponse:
    out: UpdateFlowTemplateResponse = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import aws_sdk_iotthingsgraph.types.flow_template_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.flow_template_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    return out
