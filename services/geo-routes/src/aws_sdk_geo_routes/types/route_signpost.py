"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSignpost``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_signpost_label_list


class RouteSignpost(TypedDict):
    labels: "aws_sdk_geo_routes.types.route_signpost_label_list.RouteSignpostLabelList"
    """<p>Labels present on the sign post.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSignpost) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_signpost_label_list

    out["Labels"] = aws_sdk_geo_routes.types.route_signpost_label_list.serialize_json(
        value["labels"]
    )
    return out


def deserialize_json(data: dict) -> RouteSignpost:
    out: RouteSignpost = {}  # type: ignore[typeddict-item]
    if "Labels" in data:
        import aws_sdk_geo_routes.types.route_signpost_label_list

        out["labels"] = (
            aws_sdk_geo_routes.types.route_signpost_label_list.deserialize_json(
                data["Labels"]
            )
        )
    else:
        raise DeserializationError("RouteSignpost.labels required")
    return out
