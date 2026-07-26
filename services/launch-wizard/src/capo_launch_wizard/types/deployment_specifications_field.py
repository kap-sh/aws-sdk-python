"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentSpecificationsField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.allowed_values
    import capo_launch_wizard.types.specifications_conditional_data


class DeploymentSpecificationsField(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the deployment specification.</p>"""
    description: NotRequired["str"]
    """<p>The description of the deployment specification.</p>"""
    allowed_values: NotRequired["capo_launch_wizard.types.allowed_values.AllowedValues"]
    """<p>The allowed values of the deployment specification.</p>"""
    required: NotRequired["str"]
    """<p>Indicates if the deployment specification is required.</p>"""
    conditionals: NotRequired[
        "capo_launch_wizard.types.specifications_conditional_data.SpecificationsConditionalData"
    ]
    """<p>The conditionals used for the deployment specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentSpecificationsField) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "allowed_values" in value:
        import capo_launch_wizard.types.allowed_values

        out["allowedValues"] = capo_launch_wizard.types.allowed_values.serialize_json(
            value["allowed_values"]
        )
    if "required" in value:
        out["required"] = value["required"]
    if "conditionals" in value:
        import capo_launch_wizard.types.specifications_conditional_data

        out["conditionals"] = (
            capo_launch_wizard.types.specifications_conditional_data.serialize_json(
                value["conditionals"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentSpecificationsField:
    out: DeploymentSpecificationsField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "allowedValues" in data:
        import capo_launch_wizard.types.allowed_values

        out["allowed_values"] = (
            capo_launch_wizard.types.allowed_values.deserialize_json(
                data["allowedValues"]
            )
        )
    if "required" in data:
        out["required"] = data["required"]
    if "conditionals" in data:
        import capo_launch_wizard.types.specifications_conditional_data

        out["conditionals"] = (
            capo_launch_wizard.types.specifications_conditional_data.deserialize_json(
                data["conditionals"]
            )
        )
    return out
