"""Generated from Smithy shape ``com.amazonaws.glue#Route``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.group_filters_list
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class Route(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the route node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The input connection for the route node.</p>"""
    group_filters_list: "capo_glue.types.group_filters_list.GroupFiltersList"
    """<p>A list of group filters that define the routing conditions and criteria for directing data to different output paths.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Route) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import capo_glue.types.group_filters_list

    out["GroupFiltersList"] = capo_glue.types.group_filters_list.serialize_aws_json_1_1(
        value["group_filters_list"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Route.name required")
    if "Inputs" in data:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("Route.inputs required")
    if "GroupFiltersList" in data:
        import capo_glue.types.group_filters_list

        out["group_filters_list"] = (
            capo_glue.types.group_filters_list.deserialize_aws_json_1_1(
                data["GroupFiltersList"]
            )
        )
    else:
        raise DeserializationError("Route.group_filters_list required")
    return out
