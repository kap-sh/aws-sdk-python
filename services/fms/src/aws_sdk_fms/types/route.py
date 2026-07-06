"""Generated from Smithy shape ``com.amazonaws.fms#Route``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.destination_type
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.target_type


class Route(TypedDict, closed=True):
    destination_type: NotRequired["aws_sdk_fms.types.destination_type.DestinationType"]
    """<p>The type of destination for the route.</p>"""
    target_type: NotRequired["aws_sdk_fms.types.target_type.TargetType"]
    """<p>The type of target for the route.</p>"""
    destination: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The destination of the route.</p>"""
    target: NotRequired["aws_sdk_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>The route's target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Route) -> dict:
    out: dict = {}
    if "destination_type" in value:
        import aws_sdk_fms.types.destination_type

        out["DestinationType"] = (
            aws_sdk_fms.types.destination_type.serialize_aws_json_1_1(
                value["destination_type"]
            )
        )
    if "target_type" in value:
        import aws_sdk_fms.types.target_type

        out["TargetType"] = aws_sdk_fms.types.target_type.serialize_aws_json_1_1(
            value["target_type"]
        )
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "target" in value:
        out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if "DestinationType" in data:
        import aws_sdk_fms.types.destination_type

        out["destination_type"] = (
            aws_sdk_fms.types.destination_type.deserialize_aws_json_1_1(
                data["DestinationType"]
            )
        )
    if "TargetType" in data:
        import aws_sdk_fms.types.target_type

        out["target_type"] = aws_sdk_fms.types.target_type.deserialize_aws_json_1_1(
            data["TargetType"]
        )
    if "Destination" in data:
        out["destination"] = data["Destination"]
    if "Target" in data:
        out["target"] = data["Target"]
    return out
