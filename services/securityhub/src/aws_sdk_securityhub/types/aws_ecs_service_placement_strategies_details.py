"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServicePlacementStrategiesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsServicePlacementStrategiesDetails(TypedDict, closed=True):
    field: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The field to apply the placement strategy against.</p> <p>For the <code>spread</code> placement strategy, valid values are <code>instanceId</code> (or <code>host</code>, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as <code>attribute:ecs.availability-zone</code>.</p> <p>For the <code>binpack</code> placement strategy, valid values are <code>cpu</code> and <code>memory</code>.</p> <p>For the <code>random</code> placement strategy, this attribute is not used.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of placement strategy.</p> <p>The <code>random</code> placement strategy randomly places tasks on available candidates.</p> <p>The <code>spread</code> placement strategy spreads placement across available candidates evenly based on the value of <code>Field</code>.</p> <p>The <code>binpack</code> strategy places tasks on available candidates that have the least available amount of the resource that is specified in <code>Field</code>.</p> <p>Valid values: <code>random</code> | <code>spread</code> | <code>binpack</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServicePlacementStrategiesDetails) -> dict:
    out: dict = {}
    if "field" in value:
        out["Field"] = value["field"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsEcsServicePlacementStrategiesDetails:
    out: AwsEcsServicePlacementStrategiesDetails = {}  # type: ignore[typeddict-item]
    if "Field" in data:
        out["field"] = data["Field"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
