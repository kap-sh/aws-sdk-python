"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeVirtualServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_service_data


class DescribeVirtualServiceOutput(TypedDict, closed=True):
    virtual_service: "aws_sdk_app_mesh.types.virtual_service_data.VirtualServiceData"
    """<p>The full description of your virtual service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVirtualServiceOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_service_data

    out["virtualService"] = aws_sdk_app_mesh.types.virtual_service_data.serialize_json(
        value["virtual_service"]
    )
    return out


def deserialize_json(data: dict) -> DescribeVirtualServiceOutput:
    out: DescribeVirtualServiceOutput = {}  # type: ignore[typeddict-item]
    if "virtualService" in data:
        import aws_sdk_app_mesh.types.virtual_service_data

        out["virtual_service"] = (
            aws_sdk_app_mesh.types.virtual_service_data.deserialize_json(
                data["virtualService"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeVirtualServiceOutput.virtual_service required"
        )
    return out
