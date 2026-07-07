"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdatePositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.position_coordinate
    import aws_sdk_iot_wireless.types.position_resource_identifier
    import aws_sdk_iot_wireless.types.position_resource_type


class UpdatePositionRequest(TypedDict, closed=True):
    resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier"
    """<p>Resource identifier of the resource for which position is updated.</p>"""
    resource_type: (
        "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType"
    )
    """<p>Resource type of the resource for which position is updated.</p>"""
    position: "aws_sdk_iot_wireless.types.position_coordinate.PositionCoordinate"
    """<p>The position information of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePositionRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.position_coordinate

    out["Position"] = aws_sdk_iot_wireless.types.position_coordinate.serialize_json(
        value["position"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePositionRequest:
    out: UpdatePositionRequest = {}  # type: ignore[typeddict-item]
    if "Position" in data:
        import aws_sdk_iot_wireless.types.position_coordinate

        out["position"] = (
            aws_sdk_iot_wireless.types.position_coordinate.deserialize_json(
                data["Position"]
            )
        )
    else:
        raise DeserializationError("UpdatePositionRequest.position required")
    return out
