"""Generated from Smithy shape ``com.amazonaws.vpclattice#ForwardAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.weighted_target_group_list


class ForwardAction(TypedDict, closed=True):
    target_groups: (
        "aws_sdk_vpc_lattice.types.weighted_target_group_list.WeightedTargetGroupList"
    )
    """<p>The target groups. Traffic matching the rule is forwarded to the specified target groups. With forward actions, you can assign a weight that controls the prioritization and selection of each target group. This means that requests are distributed to individual target groups based on their weights. For example, if two target groups have the same weight, each target group receives half of the traffic.</p> <p>The default value is 1. This means that if only one target group is provided, there is no need to set the weight; 100% of the traffic goes to that target group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForwardAction) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.weighted_target_group_list

    out["targetGroups"] = (
        aws_sdk_vpc_lattice.types.weighted_target_group_list.serialize_json(
            value["target_groups"]
        )
    )
    return out


def deserialize_json(data: dict) -> ForwardAction:
    out: ForwardAction = {}  # type: ignore[typeddict-item]
    if "targetGroups" in data:
        import aws_sdk_vpc_lattice.types.weighted_target_group_list

        out["target_groups"] = (
            aws_sdk_vpc_lattice.types.weighted_target_group_list.deserialize_json(
                data["targetGroups"]
            )
        )
    else:
        raise DeserializationError("ForwardAction.target_groups required")
    return out
