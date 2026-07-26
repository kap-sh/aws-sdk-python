"""Generated from Smithy shape ``com.amazonaws.apigateway#TestInvokeAuthorizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.integer
    import capo_api_gateway.types.long
    import capo_api_gateway.types.map_of_string_to_list
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string


class TestInvokeAuthorizerResponse(TypedDict, closed=True):
    client_status: "capo_api_gateway.types.integer.Integer"
    """<p>The HTTP status code that the client would have received. Value is 0 if the authorizer succeeded.</p>"""
    log: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The API Gateway execution log for the test authorizer request.</p>"""
    latency: "capo_api_gateway.types.long.Long"
    """<p>The execution latency, in ms, of the test authorizer request.</p>"""
    principal_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The principal identity returned by the Authorizer</p>"""
    policy: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The JSON policy document returned by the Authorizer</p>"""
    authorization: NotRequired[
        "capo_api_gateway.types.map_of_string_to_list.MapOfStringToList"
    ]
    """<p>The authorization response.</p>"""
    claims: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The open identity claims, with any supported custom attributes, returned from the Cognito Your User Pool configured for the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestInvokeAuthorizerResponse) -> dict:
    out: dict = {}
    out["clientStatus"] = value.get("client_status", 0)
    if "log" in value:
        out["log"] = value["log"]
    out["latency"] = value.get("latency", 0)
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "authorization" in value:
        import capo_api_gateway.types.map_of_string_to_list

        out["authorization"] = (
            capo_api_gateway.types.map_of_string_to_list.serialize_json(
                value["authorization"]
            )
        )
    if "claims" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["claims"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["claims"]
        )
    return out


def deserialize_json(data: dict) -> TestInvokeAuthorizerResponse:
    out: TestInvokeAuthorizerResponse = {}  # type: ignore[typeddict-item]
    if "clientStatus" in data:
        out["client_status"] = data["clientStatus"]
    else:
        out["client_status"] = 0
    if "log" in data:
        out["log"] = data["log"]
    if "latency" in data:
        out["latency"] = data["latency"]
    else:
        out["latency"] = 0
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    if "policy" in data:
        out["policy"] = data["policy"]
    if "authorization" in data:
        import capo_api_gateway.types.map_of_string_to_list

        out["authorization"] = (
            capo_api_gateway.types.map_of_string_to_list.deserialize_json(
                data["authorization"]
            )
        )
    if "claims" in data:
        import capo_api_gateway.types.map_of_string_to_string

        out["claims"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["claims"]
        )
    return out
