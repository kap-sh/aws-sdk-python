"""Generated from Smithy shape ``com.amazonaws.dax#CreateSubnetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dax.types.subnet_group


class CreateSubnetGroupResponse(TypedDict, closed=True):
    subnet_group: NotRequired["aws_sdk_dax.types.subnet_group.SubnetGroup"]
    """<p>Represents the output of a <i>CreateSubnetGroup</i> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubnetGroupResponse) -> dict:
    out: dict = {}
    if "subnet_group" in value:
        import aws_sdk_dax.types.subnet_group

        out["SubnetGroup"] = aws_sdk_dax.types.subnet_group.serialize_aws_json_1_1(
            value["subnet_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubnetGroupResponse:
    out: CreateSubnetGroupResponse = {}  # type: ignore[typeddict-item]
    if "SubnetGroup" in data:
        import aws_sdk_dax.types.subnet_group

        out["subnet_group"] = aws_sdk_dax.types.subnet_group.deserialize_aws_json_1_1(
            data["SubnetGroup"]
        )
    return out
