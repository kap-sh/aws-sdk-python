"""Generated from Smithy shape ``com.amazonaws.glue#GetSessionEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.session_endpoint


class GetSessionEndpointResponse(TypedDict):
    spark_connect: "aws_sdk_glue.types.session_endpoint.SessionEndpoint"
    """<p>The Spark Connect endpoint details for the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointResponse) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.session_endpoint

    out["SPARK_CONNECT"] = aws_sdk_glue.types.session_endpoint.serialize_aws_json_1_1(
        value["spark_connect"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointResponse:
    out: GetSessionEndpointResponse = {}  # type: ignore[typeddict-item]
    if "SPARK_CONNECT" in data:
        import aws_sdk_glue.types.session_endpoint

        out["spark_connect"] = (
            aws_sdk_glue.types.session_endpoint.deserialize_aws_json_1_1(
                data["SPARK_CONNECT"]
            )
        )
    else:
        raise DeserializationError("GetSessionEndpointResponse.spark_connect required")
    return out
