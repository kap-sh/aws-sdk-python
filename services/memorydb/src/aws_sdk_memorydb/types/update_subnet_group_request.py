"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateSubnetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.subnet_identifier_list


class UpdateSubnetGroupRequest(TypedDict, closed=True):
    subnet_group_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the subnet group</p>"""
    description: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>A description of the subnet group</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_memorydb.types.subnet_identifier_list.SubnetIdentifierList"
    ]
    """<p>The EC2 subnet IDs for the subnet group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubnetGroupRequest) -> dict:
    out: dict = {}
    out["SubnetGroupName"] = value["subnet_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "subnet_ids" in value:
        import aws_sdk_memorydb.types.subnet_identifier_list

        out["SubnetIds"] = (
            aws_sdk_memorydb.types.subnet_identifier_list.serialize_aws_json_1_1(
                value["subnet_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubnetGroupRequest:
    out: UpdateSubnetGroupRequest = {}  # type: ignore[typeddict-item]
    if "SubnetGroupName" in data:
        out["subnet_group_name"] = data["SubnetGroupName"]
    else:
        raise DeserializationError(
            "UpdateSubnetGroupRequest.subnet_group_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "SubnetIds" in data:
        import aws_sdk_memorydb.types.subnet_identifier_list

        out["subnet_ids"] = (
            aws_sdk_memorydb.types.subnet_identifier_list.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    return out
