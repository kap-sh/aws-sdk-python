"""Generated from Smithy shape ``com.amazonaws.controlcatalog#RegionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.control_scope
    import aws_sdk_controlcatalog.types.deployable_regions


class RegionConfiguration(TypedDict):
    scope: "aws_sdk_controlcatalog.types.control_scope.ControlScope"
    """<p>The coverage of the control, if deployed. Scope is an enumerated type, with value <code>Regional</code>, or <code>Global</code>. A control with Global scope is effective in all Amazon Web Services Regions, regardless of the Region from which it is enabled, or to which it is deployed. A control implemented by an SCP is usually Global in scope. A control with Regional scope has operations that are restricted specifically to the Region from which it is enabled and to which it is deployed. Controls implemented by Config rules and CloudFormation hooks usually are Regional in scope. Security Hub controls usually are Regional in scope.</p>"""
    deployable_regions: NotRequired[
        "aws_sdk_controlcatalog.types.deployable_regions.DeployableRegions"
    ]
    """<p>Regions in which the control is available to be deployed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_controlcatalog.types.control_scope

    out["Scope"] = aws_sdk_controlcatalog.types.control_scope.serialize_json(
        value["scope"]
    )
    if "deployable_regions" in value:
        import aws_sdk_controlcatalog.types.deployable_regions

        out["DeployableRegions"] = (
            aws_sdk_controlcatalog.types.deployable_regions.serialize_json(
                value["deployable_regions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegionConfiguration:
    out: RegionConfiguration = {}  # type: ignore[typeddict-item]
    if "Scope" in data:
        import aws_sdk_controlcatalog.types.control_scope

        out["scope"] = aws_sdk_controlcatalog.types.control_scope.deserialize_json(
            data["Scope"]
        )
    else:
        raise DeserializationError("RegionConfiguration.scope required")
    if "DeployableRegions" in data:
        import aws_sdk_controlcatalog.types.deployable_regions

        out["deployable_regions"] = (
            aws_sdk_controlcatalog.types.deployable_regions.deserialize_json(
                data["DeployableRegions"]
            )
        )
    return out
