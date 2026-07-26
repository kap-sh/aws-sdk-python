"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollRate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll_pass
    import capo_geo_routes.types.route_toll_payment_method_list
    import capo_geo_routes.types.route_toll_price
    import capo_geo_routes.types.route_transponder_list
    import capo_geo_routes.types.sensitive_string

RouteTollRate = TypedDict(
    "RouteTollRate",
    {
        "applicable_times": NotRequired[
            "capo_geo_routes.types.sensitive_string.SensitiveString"
        ],
        "converted_price": NotRequired[
            "capo_geo_routes.types.route_toll_price.RouteTollPrice"
        ],
        "id": "capo_geo_routes.types.sensitive_string.SensitiveString",
        "local_price": "capo_geo_routes.types.route_toll_price.RouteTollPrice",
        "name": "capo_geo_routes.types.sensitive_string.SensitiveString",
        "pass": NotRequired["capo_geo_routes.types.route_toll_pass.RouteTollPass"],
        "payment_methods": "capo_geo_routes.types.route_toll_payment_method_list.RouteTollPaymentMethodList",
        "transponders": "capo_geo_routes.types.route_transponder_list.RouteTransponderList",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollRate) -> dict:
    out: dict = {}
    if "applicable_times" in value:
        out["ApplicableTimes"] = value["applicable_times"]
    if "converted_price" in value:
        import capo_geo_routes.types.route_toll_price

        out["ConvertedPrice"] = capo_geo_routes.types.route_toll_price.serialize_json(
            value["converted_price"]
        )
    out["Id"] = value["id"]
    import capo_geo_routes.types.route_toll_price

    out["LocalPrice"] = capo_geo_routes.types.route_toll_price.serialize_json(
        value["local_price"]
    )
    out["Name"] = value["name"]
    if "pass" in value:
        import capo_geo_routes.types.route_toll_pass

        out["Pass"] = capo_geo_routes.types.route_toll_pass.serialize_json(
            value["pass"]
        )
    import capo_geo_routes.types.route_toll_payment_method_list

    out["PaymentMethods"] = (
        capo_geo_routes.types.route_toll_payment_method_list.serialize_json(
            value["payment_methods"]
        )
    )
    import capo_geo_routes.types.route_transponder_list

    out["Transponders"] = capo_geo_routes.types.route_transponder_list.serialize_json(
        value["transponders"]
    )
    return out


def deserialize_json(data: dict) -> RouteTollRate:
    out: RouteTollRate = {}  # type: ignore[typeddict-item]
    if "ApplicableTimes" in data:
        out["applicable_times"] = data["ApplicableTimes"]
    if "ConvertedPrice" in data:
        import capo_geo_routes.types.route_toll_price

        out["converted_price"] = (
            capo_geo_routes.types.route_toll_price.deserialize_json(
                data["ConvertedPrice"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("RouteTollRate.id required")
    if "LocalPrice" in data:
        import capo_geo_routes.types.route_toll_price

        out["local_price"] = capo_geo_routes.types.route_toll_price.deserialize_json(
            data["LocalPrice"]
        )
    else:
        raise DeserializationError("RouteTollRate.local_price required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RouteTollRate.name required")
    if "Pass" in data:
        import capo_geo_routes.types.route_toll_pass

        out["pass"] = capo_geo_routes.types.route_toll_pass.deserialize_json(
            data["Pass"]
        )
    if "PaymentMethods" in data:
        import capo_geo_routes.types.route_toll_payment_method_list

        out["payment_methods"] = (
            capo_geo_routes.types.route_toll_payment_method_list.deserialize_json(
                data["PaymentMethods"]
            )
        )
    else:
        raise DeserializationError("RouteTollRate.payment_methods required")
    if "Transponders" in data:
        import capo_geo_routes.types.route_transponder_list

        out["transponders"] = (
            capo_geo_routes.types.route_transponder_list.deserialize_json(
                data["Transponders"]
            )
        )
    else:
        raise DeserializationError("RouteTollRate.transponders required")
    return out
