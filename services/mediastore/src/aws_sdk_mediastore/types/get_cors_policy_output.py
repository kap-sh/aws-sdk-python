"""Generated from Smithy shape ``com.amazonaws.mediastore#GetCorsPolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.cors_policy


class GetCorsPolicyOutput(TypedDict):
    cors_policy: "aws_sdk_mediastore.types.cors_policy.CorsPolicy"
    """<p>The CORS policy assigned to the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCorsPolicyOutput) -> dict:
    out: dict = {}
    import aws_sdk_mediastore.types.cors_policy

    out["CorsPolicy"] = aws_sdk_mediastore.types.cors_policy.serialize_aws_json_1_1(
        value["cors_policy"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCorsPolicyOutput:
    out: GetCorsPolicyOutput = {}  # type: ignore[typeddict-item]
    if "CorsPolicy" in data:
        import aws_sdk_mediastore.types.cors_policy

        out["cors_policy"] = (
            aws_sdk_mediastore.types.cors_policy.deserialize_aws_json_1_1(
                data["CorsPolicy"]
            )
        )
    else:
        raise DeserializationError("GetCorsPolicyOutput.cors_policy required")
    return out
