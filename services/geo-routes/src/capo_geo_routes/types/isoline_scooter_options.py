"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineScooterOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_engine_type
    import capo_geo_routes.types.isoline_vehicle_license_plate
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.speed_kilometers_per_hour


class IsolineScooterOptions(TypedDict, closed=True):
    engine_type: NotRequired[
        "capo_geo_routes.types.isoline_engine_type.IsolineEngineType"
    ]
    """<p>The type of engine powering the vehicle, which may affect route calculation due to road restrictions or vehicle characteristics.</p> <ul> <li> <p> <code>INTERNAL_COMBUSTION</code>—Standard gasoline or diesel engine.</p> </li> <li> <p> <code>ELECTRIC</code>—Battery electric vehicle.</p> </li> <li> <p> <code>PLUGIN_HYBRID</code>—Combination of electric and internal combustion engines with plug-in charging capability.</p> </li> </ul>"""
    license_plate: NotRequired[
        "capo_geo_routes.types.isoline_vehicle_license_plate.IsolineVehicleLicensePlate"
    ]
    """<p>License plate information used in regions where road access or routing restrictions are based on license plate numbers.</p>"""
    max_speed: NotRequired[
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>The maximum speed of the vehicle in kilometers per hour. When specified, routes will not include roads with higher speed limits. Valid values range from 3.6 km/h (1 m/s) to 252 km/h (70 m/s).</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    occupancy: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>The number of occupants in the vehicle. This can affect route calculations by enabling the use of high-occupancy vehicle (HOV) lanes where minimum occupancy requirements are met.</p> <p>Default value: <code>1</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineScooterOptions) -> dict:
    out: dict = {}
    if "engine_type" in value:
        import capo_geo_routes.types.isoline_engine_type

        out["EngineType"] = capo_geo_routes.types.isoline_engine_type.serialize_json(
            value["engine_type"]
        )
    if "license_plate" in value:
        import capo_geo_routes.types.isoline_vehicle_license_plate

        out["LicensePlate"] = (
            capo_geo_routes.types.isoline_vehicle_license_plate.serialize_json(
                value["license_plate"]
            )
        )
    if "max_speed" in value:
        out["MaxSpeed"] = value["max_speed"]
    if "occupancy" in value:
        out["Occupancy"] = value["occupancy"]
    return out


def deserialize_json(data: dict) -> IsolineScooterOptions:
    out: IsolineScooterOptions = {}  # type: ignore[typeddict-item]
    if "EngineType" in data:
        import capo_geo_routes.types.isoline_engine_type

        out["engine_type"] = capo_geo_routes.types.isoline_engine_type.deserialize_json(
            data["EngineType"]
        )
    if "LicensePlate" in data:
        import capo_geo_routes.types.isoline_vehicle_license_plate

        out["license_plate"] = (
            capo_geo_routes.types.isoline_vehicle_license_plate.deserialize_json(
                data["LicensePlate"]
            )
        )
    if "MaxSpeed" in data:
        out["max_speed"] = data["MaxSpeed"]
    if "Occupancy" in data:
        out["occupancy"] = data["Occupancy"]
    return out
