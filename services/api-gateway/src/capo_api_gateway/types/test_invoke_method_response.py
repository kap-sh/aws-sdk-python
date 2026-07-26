"""Generated from Smithy shape ``com.amazonaws.apigateway#TestInvokeMethodResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.integer
    import capo_api_gateway.types.long
    import capo_api_gateway.types.map_of_string_to_list
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string


class TestInvokeMethodResponse(TypedDict, closed=True):
    status: "capo_api_gateway.types.integer.Integer"
    """<p>The HTTP status code.</p>"""
    body: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The body of the HTTP response.</p>"""
    headers: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The headers of the HTTP response.</p>"""
    multi_value_headers: NotRequired[
        "capo_api_gateway.types.map_of_string_to_list.MapOfStringToList"
    ]
    """<p>The headers of the HTTP response as a map from string to list of values.</p>"""
    log: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The API Gateway execution log for the test invoke request.</p>"""
    latency: "capo_api_gateway.types.long.Long"
    """<p>The execution latency, in ms, of the test invoke request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestInvokeMethodResponse) -> dict:
    out: dict = {}
    out["status"] = value.get("status", 0)
    if "body" in value:
        out["body"] = value["body"]
    if "headers" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["headers"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["headers"]
        )
    if "multi_value_headers" in value:
        import capo_api_gateway.types.map_of_string_to_list

        out["multiValueHeaders"] = (
            capo_api_gateway.types.map_of_string_to_list.serialize_json(
                value["multi_value_headers"]
            )
        )
    if "log" in value:
        out["log"] = value["log"]
    out["latency"] = value.get("latency", 0)
    return out


def deserialize_json(data: dict) -> TestInvokeMethodResponse:
    out: TestInvokeMethodResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        out["status"] = 0
    if "body" in data:
        out["body"] = data["body"]
    if "headers" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["headers"] = (
            capo_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["headers"]
            )
        )
    if "multiValueHeaders" in data:
        import capo_api_gateway.types.map_of_string_to_list

        out["multi_value_headers"] = (
            capo_api_gateway.types.map_of_string_to_list.deserialize_json(
                data["multiValueHeaders"]
            )
        )
    if "log" in data:
        out["log"] = data["log"]
    if "latency" in data:
        out["latency"] = data["latency"]
    else:
        out["latency"] = 0
    return out
