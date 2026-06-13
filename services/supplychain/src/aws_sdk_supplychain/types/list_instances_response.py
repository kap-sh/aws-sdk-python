"""Generated from Smithy shape ``com.amazonaws.supplychain#ListInstancesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.instance_list
    import aws_sdk_supplychain.types.instance_next_token


class ListInstancesResponse(TypedDict):
    instances: "aws_sdk_supplychain.types.instance_list.InstanceList"
    """<p>The list of instances resource data details.</p>"""
    next_token: NotRequired[
        "aws_sdk_supplychain.types.instance_next_token.InstanceNextToken"
    ]
    """<p>The pagination token to fetch the next page of instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstancesResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.instance_list

    out["instances"] = aws_sdk_supplychain.types.instance_list.serialize_json(
        value["instances"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstancesResponse:
    out: ListInstancesResponse = {}  # type: ignore[typeddict-item]
    if "instances" in data:
        import aws_sdk_supplychain.types.instance_list

        out["instances"] = aws_sdk_supplychain.types.instance_list.deserialize_json(
            data["instances"]
        )
    else:
        raise DeserializationError("ListInstancesResponse.instances required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
