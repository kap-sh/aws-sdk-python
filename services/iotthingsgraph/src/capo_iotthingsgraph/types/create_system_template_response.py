"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#CreateSystemTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.system_template_summary


class CreateSystemTemplateResponse(TypedDict, closed=True):
    summary: NotRequired[
        "capo_iotthingsgraph.types.system_template_summary.SystemTemplateSummary"
    ]
    """<p>The summary object that describes the created system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSystemTemplateResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import capo_iotthingsgraph.types.system_template_summary

        out["summary"] = (
            capo_iotthingsgraph.types.system_template_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSystemTemplateResponse:
    out: CreateSystemTemplateResponse = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import capo_iotthingsgraph.types.system_template_summary

        out["summary"] = (
            capo_iotthingsgraph.types.system_template_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    return out
