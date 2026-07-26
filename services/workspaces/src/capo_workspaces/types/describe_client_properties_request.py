"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeClientPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.resource_id_list


class DescribeClientPropertiesRequest(TypedDict, closed=True):
    resource_ids: "capo_workspaces.types.resource_id_list.ResourceIdList"
    """<p>The resource identifier, in the form of directory IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClientPropertiesRequest) -> dict:
    out: dict = {}
    import capo_workspaces.types.resource_id_list

    out["ResourceIds"] = capo_workspaces.types.resource_id_list.serialize_aws_json_1_1(
        value["resource_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClientPropertiesRequest:
    out: DescribeClientPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceIds" in data:
        import capo_workspaces.types.resource_id_list

        out["resource_ids"] = (
            capo_workspaces.types.resource_id_list.deserialize_aws_json_1_1(
                data["ResourceIds"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeClientPropertiesRequest.resource_ids required"
        )
    return out
