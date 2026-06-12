"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTravelModeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.isoline_car_options
    import aws_sdk_geo_routes.types.isoline_scooter_options
    import aws_sdk_geo_routes.types.isoline_truck_options


class IsolineTravelModeOptions(TypedDict):
    car: NotRequired["aws_sdk_geo_routes.types.isoline_car_options.IsolineCarOptions"]
    """<p>Options specific to passenger vehicle routing (<code>Car</code>, such as vehicle characteristics and license plate restrictions.</p>"""
    scooter: NotRequired[
        "aws_sdk_geo_routes.types.isoline_scooter_options.IsolineScooterOptions"
    ]
    """<p>Options specific to scooter routing (<code>Scooter</code>, such as vehicle characteristics and license plate restrictions.</p> <note> <p>When using the <code>Scooter</code> travel mode, controlled-access highways are automatically avoided unless explicitly allowed.</p> </note>"""
    truck: NotRequired[
        "aws_sdk_geo_routes.types.isoline_truck_options.IsolineTruckOptions"
    ]
    """<p>Options specific to commercial truck routing (<code>Truck</code>, including vehicle dimensions, weight limits, and hazardous cargo specifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineTravelModeOptions) -> dict:
    out: dict = {}
    if "car" in value:
        import aws_sdk_geo_routes.types.isoline_car_options

        out["Car"] = aws_sdk_geo_routes.types.isoline_car_options.serialize_json(
            value["car"]
        )
    if "scooter" in value:
        import aws_sdk_geo_routes.types.isoline_scooter_options

        out["Scooter"] = (
            aws_sdk_geo_routes.types.isoline_scooter_options.serialize_json(
                value["scooter"]
            )
        )
    if "truck" in value:
        import aws_sdk_geo_routes.types.isoline_truck_options

        out["Truck"] = aws_sdk_geo_routes.types.isoline_truck_options.serialize_json(
            value["truck"]
        )
    return out


def deserialize_json(data: dict) -> IsolineTravelModeOptions:
    out: IsolineTravelModeOptions = {}  # type: ignore[typeddict-item]
    if "Car" in data:
        import aws_sdk_geo_routes.types.isoline_car_options

        out["car"] = aws_sdk_geo_routes.types.isoline_car_options.deserialize_json(
            data["Car"]
        )
    if "Scooter" in data:
        import aws_sdk_geo_routes.types.isoline_scooter_options

        out["scooter"] = (
            aws_sdk_geo_routes.types.isoline_scooter_options.deserialize_json(
                data["Scooter"]
            )
        )
    if "Truck" in data:
        import aws_sdk_geo_routes.types.isoline_truck_options

        out["truck"] = aws_sdk_geo_routes.types.isoline_truck_options.deserialize_json(
            data["Truck"]
        )
    return out
