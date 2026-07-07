"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetServiceViewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.service_view


class GetServiceViewOutput(TypedDict, closed=True):
    view: "aws_sdk_resource_explorer_2.types.service_view.ServiceView"
    """<p>A <code>ServiceView</code> object that contains the details and configuration of the requested service view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceViewOutput) -> dict:
    out: dict = {}
    import aws_sdk_resource_explorer_2.types.service_view

    out["View"] = aws_sdk_resource_explorer_2.types.service_view.serialize_json(
        value["view"]
    )
    return out


def deserialize_json(data: dict) -> GetServiceViewOutput:
    out: GetServiceViewOutput = {}  # type: ignore[typeddict-item]
    if "View" in data:
        import aws_sdk_resource_explorer_2.types.service_view

        out["view"] = aws_sdk_resource_explorer_2.types.service_view.deserialize_json(
            data["View"]
        )
    else:
        raise DeserializationError("GetServiceViewOutput.view required")
    return out
