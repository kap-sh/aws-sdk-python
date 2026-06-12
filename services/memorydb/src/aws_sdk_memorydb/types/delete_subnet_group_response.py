"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteSubnetGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.subnet_group


class DeleteSubnetGroupResponse(TypedDict):
    subnet_group: NotRequired["aws_sdk_memorydb.types.subnet_group.SubnetGroup"]
    """<p>The subnet group object that has been deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSubnetGroupResponse) -> dict:
    out: dict = {}
    if "subnet_group" in value:
        import aws_sdk_memorydb.types.subnet_group

        out["SubnetGroup"] = aws_sdk_memorydb.types.subnet_group.serialize_aws_json_1_1(
            value["subnet_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSubnetGroupResponse:
    out: DeleteSubnetGroupResponse = {}  # type: ignore[typeddict-item]
    if "SubnetGroup" in data:
        import aws_sdk_memorydb.types.subnet_group

        out["subnet_group"] = (
            aws_sdk_memorydb.types.subnet_group.deserialize_aws_json_1_1(
                data["SubnetGroup"]
            )
        )
    return out
