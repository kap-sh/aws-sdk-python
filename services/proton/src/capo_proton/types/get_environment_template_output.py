"""Generated from Smithy shape ``com.amazonaws.proton#GetEnvironmentTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment_template


class GetEnvironmentTemplateOutput(TypedDict, closed=True):
    environment_template: "capo_proton.types.environment_template.EnvironmentTemplate"
    """<p>The detailed data of the requested environment template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentTemplateOutput) -> dict:
    out: dict = {}
    import capo_proton.types.environment_template

    out["environmentTemplate"] = (
        capo_proton.types.environment_template.serialize_aws_json_1_0(
            value["environment_template"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentTemplateOutput:
    out: GetEnvironmentTemplateOutput = {}  # type: ignore[typeddict-item]
    if "environmentTemplate" in data:
        import capo_proton.types.environment_template

        out["environment_template"] = (
            capo_proton.types.environment_template.deserialize_aws_json_1_0(
                data["environmentTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnvironmentTemplateOutput.environment_template required"
        )
    return out
