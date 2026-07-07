"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpQueryParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.query_parameter_match
    import aws_sdk_app_mesh.types.query_parameter_name


class HttpQueryParameter(TypedDict, closed=True):
    name: "aws_sdk_app_mesh.types.query_parameter_name.QueryParameterName"
    """<p>A name for the query parameter that will be matched on.</p>"""
    match: NotRequired[
        "aws_sdk_app_mesh.types.query_parameter_match.QueryParameterMatch"
    ]
    """<p>The query parameter to match on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpQueryParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "match" in value:
        import aws_sdk_app_mesh.types.query_parameter_match

        out["match"] = aws_sdk_app_mesh.types.query_parameter_match.serialize_json(
            value["match"]
        )
    return out


def deserialize_json(data: dict) -> HttpQueryParameter:
    out: HttpQueryParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("HttpQueryParameter.name required")
    if "match" in data:
        import aws_sdk_app_mesh.types.query_parameter_match

        out["match"] = aws_sdk_app_mesh.types.query_parameter_match.deserialize_json(
            data["match"]
        )
    return out
