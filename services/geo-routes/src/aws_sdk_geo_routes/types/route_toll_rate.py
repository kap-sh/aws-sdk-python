"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollRate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_toll_pass
    import aws_sdk_geo_routes.types.route_toll_payment_method_list
    import aws_sdk_geo_routes.types.route_toll_price
    import aws_sdk_geo_routes.types.route_transponder_list
    import aws_sdk_geo_routes.types.sensitive_string

RouteTollRate = TypedDict(
    "RouteTollRate",
    {
        "applicable_times": NotRequired[
            "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
        ],
        "converted_price": NotRequired[
            "aws_sdk_geo_routes.types.route_toll_price.RouteTollPrice"
        ],
        "id": "aws_sdk_geo_routes.types.sensitive_string.SensitiveString",
        "local_price": "aws_sdk_geo_routes.types.route_toll_price.RouteTollPrice",
        "name": "aws_sdk_geo_routes.types.sensitive_string.SensitiveString",
        "pass": NotRequired["aws_sdk_geo_routes.types.route_toll_pass.RouteTollPass"],
        "payment_methods": "aws_sdk_geo_routes.types.route_toll_payment_method_list.RouteTollPaymentMethodList",
        "transponders": "aws_sdk_geo_routes.types.route_transponder_list.RouteTransponderList",
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollRate) -> dict:
    out: dict = {}
    if "applicable_times" in value:
        out["ApplicableTimes"] = value["applicable_times"]
    if "converted_price" in value:
        import aws_sdk_geo_routes.types.route_toll_price

        out["ConvertedPrice"] = (
            aws_sdk_geo_routes.types.route_toll_price.serialize_json(
                value["converted_price"]
            )
        )
    out["Id"] = value["id"]
    import aws_sdk_geo_routes.types.route_toll_price

    out["LocalPrice"] = aws_sdk_geo_routes.types.route_toll_price.serialize_json(
        value["local_price"]
    )
    out["Name"] = value["name"]
    if "pass" in value:
        import aws_sdk_geo_routes.types.route_toll_pass

        out["Pass"] = aws_sdk_geo_routes.types.route_toll_pass.serialize_json(
            value["pass"]
        )
    import aws_sdk_geo_routes.types.route_toll_payment_method_list

    out["PaymentMethods"] = (
        aws_sdk_geo_routes.types.route_toll_payment_method_list.serialize_json(
            value["payment_methods"]
        )
    )
    import aws_sdk_geo_routes.types.route_transponder_list

    out["Transponders"] = (
        aws_sdk_geo_routes.types.route_transponder_list.serialize_json(
            value["transponders"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteTollRate:
    out: RouteTollRate = {}  # type: ignore[typeddict-item]
    if "ApplicableTimes" in data:
        out["applicable_times"] = data["ApplicableTimes"]
    if "ConvertedPrice" in data:
        import aws_sdk_geo_routes.types.route_toll_price

        out["converted_price"] = (
            aws_sdk_geo_routes.types.route_toll_price.deserialize_json(
                data["ConvertedPrice"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("RouteTollRate.id required")
    if "LocalPrice" in data:
        import aws_sdk_geo_routes.types.route_toll_price

        out["local_price"] = aws_sdk_geo_routes.types.route_toll_price.deserialize_json(
            data["LocalPrice"]
        )
    else:
        raise DeserializationError("RouteTollRate.local_price required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RouteTollRate.name required")
    if "Pass" in data:
        import aws_sdk_geo_routes.types.route_toll_pass

        out["pass"] = aws_sdk_geo_routes.types.route_toll_pass.deserialize_json(
            data["Pass"]
        )
    if "PaymentMethods" in data:
        import aws_sdk_geo_routes.types.route_toll_payment_method_list

        out["payment_methods"] = (
            aws_sdk_geo_routes.types.route_toll_payment_method_list.deserialize_json(
                data["PaymentMethods"]
            )
        )
    else:
        raise DeserializationError("RouteTollRate.payment_methods required")
    if "Transponders" in data:
        import aws_sdk_geo_routes.types.route_transponder_list

        out["transponders"] = (
            aws_sdk_geo_routes.types.route_transponder_list.deserialize_json(
                data["Transponders"]
            )
        )
    else:
        raise DeserializationError("RouteTollRate.transponders required")
    return out
