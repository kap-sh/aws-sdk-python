"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetProfileTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_template


class GetProfileTemplateOutput(TypedDict):
    profile_template: NotRequired[
        "aws_sdk_wellarchitected.types.profile_template.ProfileTemplate"
    ]
    """<p>The profile template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileTemplateOutput) -> dict:
    out: dict = {}
    if "profile_template" in value:
        import aws_sdk_wellarchitected.types.profile_template

        out["ProfileTemplate"] = (
            aws_sdk_wellarchitected.types.profile_template.serialize_json(
                value["profile_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetProfileTemplateOutput:
    out: GetProfileTemplateOutput = {}  # type: ignore[typeddict-item]
    if "ProfileTemplate" in data:
        import aws_sdk_wellarchitected.types.profile_template

        out["profile_template"] = (
            aws_sdk_wellarchitected.types.profile_template.deserialize_json(
                data["ProfileTemplate"]
            )
        )
    return out
