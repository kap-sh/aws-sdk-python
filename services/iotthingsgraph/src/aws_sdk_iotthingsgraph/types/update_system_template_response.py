"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UpdateSystemTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_template_summary


class UpdateSystemTemplateResponse(TypedDict):
    summary: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_template_summary.SystemTemplateSummary"
    ]
    """<p>An object containing summary information about the updated system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSystemTemplateResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import aws_sdk_iotthingsgraph.types.system_template_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_template_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSystemTemplateResponse:
    out: UpdateSystemTemplateResponse = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import aws_sdk_iotthingsgraph.types.system_template_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_template_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    return out
