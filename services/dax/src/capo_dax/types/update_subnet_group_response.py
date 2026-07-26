"""Generated from Smithy shape ``com.amazonaws.dax#UpdateSubnetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.subnet_group


class UpdateSubnetGroupResponse(TypedDict, closed=True):
    subnet_group: NotRequired["capo_dax.types.subnet_group.SubnetGroup"]
    """<p>The subnet group that has been modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubnetGroupResponse) -> dict:
    out: dict = {}
    if "subnet_group" in value:
        import capo_dax.types.subnet_group

        out["SubnetGroup"] = capo_dax.types.subnet_group.serialize_aws_json_1_1(
            value["subnet_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubnetGroupResponse:
    out: UpdateSubnetGroupResponse = {}  # type: ignore[typeddict-item]
    if "SubnetGroup" in data:
        import capo_dax.types.subnet_group

        out["subnet_group"] = capo_dax.types.subnet_group.deserialize_aws_json_1_1(
            data["SubnetGroup"]
        )
    return out
