"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#GetResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.resource_description
    import capo_cloudcontrol.types.type_name


class GetResourceOutput(TypedDict, closed=True):
    type_name: NotRequired["capo_cloudcontrol.types.type_name.TypeName"]
    """<p>The name of the resource type.</p>"""
    resource_description: NotRequired[
        "capo_cloudcontrol.types.resource_description.ResourceDescription"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceOutput) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "resource_description" in value:
        import capo_cloudcontrol.types.resource_description

        out["ResourceDescription"] = (
            capo_cloudcontrol.types.resource_description.serialize_aws_json_1_0(
                value["resource_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceOutput:
    out: GetResourceOutput = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "ResourceDescription" in data:
        import capo_cloudcontrol.types.resource_description

        out["resource_description"] = (
            capo_cloudcontrol.types.resource_description.deserialize_aws_json_1_0(
                data["ResourceDescription"]
            )
        )
    return out
