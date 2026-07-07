"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeVirtualRouterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_router_data


class DescribeVirtualRouterOutput(TypedDict, closed=True):
    virtual_router: "aws_sdk_app_mesh.types.virtual_router_data.VirtualRouterData"
    """<p>The full description of your virtual router.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVirtualRouterOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_router_data

    out["virtualRouter"] = aws_sdk_app_mesh.types.virtual_router_data.serialize_json(
        value["virtual_router"]
    )
    return out


def deserialize_json(data: dict) -> DescribeVirtualRouterOutput:
    out: DescribeVirtualRouterOutput = {}  # type: ignore[typeddict-item]
    if "virtualRouter" in data:
        import aws_sdk_app_mesh.types.virtual_router_data

        out["virtual_router"] = (
            aws_sdk_app_mesh.types.virtual_router_data.deserialize_json(
                data["virtualRouter"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeVirtualRouterOutput.virtual_router required"
        )
    return out
