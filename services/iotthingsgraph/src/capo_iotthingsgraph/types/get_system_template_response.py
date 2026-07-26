"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetSystemTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.system_template_description


class GetSystemTemplateResponse(TypedDict, closed=True):
    description: NotRequired[
        "capo_iotthingsgraph.types.system_template_description.SystemTemplateDescription"
    ]
    """<p>An object that contains summary data about the system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemTemplateResponse) -> dict:
    out: dict = {}
    if "description" in value:
        import capo_iotthingsgraph.types.system_template_description

        out["description"] = (
            capo_iotthingsgraph.types.system_template_description.serialize_aws_json_1_1(
                value["description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemTemplateResponse:
    out: GetSystemTemplateResponse = {}  # type: ignore[typeddict-item]
    if "description" in data:
        import capo_iotthingsgraph.types.system_template_description

        out["description"] = (
            capo_iotthingsgraph.types.system_template_description.deserialize_aws_json_1_1(
                data["description"]
            )
        )
    return out
