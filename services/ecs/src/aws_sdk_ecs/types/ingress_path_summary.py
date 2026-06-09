"""Generated from Smithy shape ``com.amazonaws.ecs#IngressPathSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.access_type
    import aws_sdk_ecs.types.string


class IngressPathSummary(TypedDict):
    access_type: "aws_sdk_ecs.types.access_type.AccessType"
    """<p>The type of access to the endpoint for the Express service.</p>"""
    endpoint: "aws_sdk_ecs.types.string.String"
    """<p>The endpoint for access to the service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IngressPathSummary) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.access_type

    out["accessType"] = aws_sdk_ecs.types.access_type.serialize_aws_json_1_1(
        value["access_type"]
    )
    out["endpoint"] = value["endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IngressPathSummary:
    out: IngressPathSummary = {}  # type: ignore[typeddict-item]
    if "accessType" in data:
        import aws_sdk_ecs.types.access_type

        out["access_type"] = aws_sdk_ecs.types.access_type.deserialize_aws_json_1_1(
            data["accessType"]
        )
    else:
        raise DeserializationError("IngressPathSummary.access_type required")
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("IngressPathSummary.endpoint required")
    return out
