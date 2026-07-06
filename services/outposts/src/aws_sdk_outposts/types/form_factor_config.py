"""Generated from Smithy shape ``com.amazonaws.outposts#FormFactorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.form_factor
    import aws_sdk_outposts.types.outpost_generation


class FormFactorConfig(TypedDict, closed=True):
    form_factor: NotRequired["aws_sdk_outposts.types.form_factor.FormFactor"]
    """<p>The form factor. Valid values are <code>RACK</code> for rack-based Outposts and <code>SERVER</code> for server-based Outposts.</p>"""
    outpost_generation: NotRequired[
        "aws_sdk_outposts.types.outpost_generation.OutpostGeneration"
    ]
    """<p>The Outpost generation. Valid values are <code>GENERATION_1</code> for first-generation rack deployments and <code>GENERATION_2</code> for second-generation rack deployments. This value is not set for server form factors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormFactorConfig) -> dict:
    out: dict = {}
    if "form_factor" in value:
        import aws_sdk_outposts.types.form_factor

        out["FormFactor"] = aws_sdk_outposts.types.form_factor.serialize_json(
            value["form_factor"]
        )
    if "outpost_generation" in value:
        import aws_sdk_outposts.types.outpost_generation

        out["OutpostGeneration"] = (
            aws_sdk_outposts.types.outpost_generation.serialize_json(
                value["outpost_generation"]
            )
        )
    return out


def deserialize_json(data: dict) -> FormFactorConfig:
    out: FormFactorConfig = {}  # type: ignore[typeddict-item]
    if "FormFactor" in data:
        import aws_sdk_outposts.types.form_factor

        out["form_factor"] = aws_sdk_outposts.types.form_factor.deserialize_json(
            data["FormFactor"]
        )
    if "OutpostGeneration" in data:
        import aws_sdk_outposts.types.outpost_generation

        out["outpost_generation"] = (
            aws_sdk_outposts.types.outpost_generation.deserialize_json(
                data["OutpostGeneration"]
            )
        )
    return out
