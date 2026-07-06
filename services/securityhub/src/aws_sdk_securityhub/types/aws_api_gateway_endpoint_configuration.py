"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiGatewayEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsApiGatewayEndpointConfiguration(TypedDict, closed=True):
    types: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>A list of endpoint types for the REST API.</p> <p>For an edge-optimized API, the endpoint type is <code>EDGE</code>. For a Regional API, the endpoint type is <code>REGIONAL</code>. For a private API, the endpoint type is <code>PRIVATE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiGatewayEndpointConfiguration) -> dict:
    out: dict = {}
    if "types" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["Types"] = aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
            value["types"]
        )
    return out


def deserialize_json(data: dict) -> AwsApiGatewayEndpointConfiguration:
    out: AwsApiGatewayEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if "Types" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["types"] = aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
            data["Types"]
        )
    return out
