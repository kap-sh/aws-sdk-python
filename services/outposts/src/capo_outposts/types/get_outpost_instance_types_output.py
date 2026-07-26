"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostInstanceTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.instance_type_list_definition
    import capo_outposts.types.outpost_arn
    import capo_outposts.types.outpost_id
    import capo_outposts.types.token


class GetOutpostInstanceTypesOutput(TypedDict, closed=True):
    instance_types: NotRequired[
        "capo_outposts.types.instance_type_list_definition.InstanceTypeListDefinition"
    ]
    next_token: NotRequired["capo_outposts.types.token.Token"]
    outpost_id: NotRequired["capo_outposts.types.outpost_id.OutpostId"]
    """<p> The ID of the Outpost. </p>"""
    outpost_arn: NotRequired["capo_outposts.types.outpost_arn.OutpostArn"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostInstanceTypesOutput) -> dict:
    out: dict = {}
    if "instance_types" in value:
        import capo_outposts.types.instance_type_list_definition

        out["InstanceTypes"] = (
            capo_outposts.types.instance_type_list_definition.serialize_json(
                value["instance_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    return out


def deserialize_json(data: dict) -> GetOutpostInstanceTypesOutput:
    out: GetOutpostInstanceTypesOutput = {}  # type: ignore[typeddict-item]
    if "InstanceTypes" in data:
        import capo_outposts.types.instance_type_list_definition

        out["instance_types"] = (
            capo_outposts.types.instance_type_list_definition.deserialize_json(
                data["InstanceTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    return out
