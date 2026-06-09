"""Generated from Smithy shape ``com.amazonaws.ecs#CreatedAt``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.timestamp


class CreatedAt(TypedDict):
    before: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>Include service deployments in the result that were created before this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    after: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>Include service deployments in the result that were created after this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedAt) -> dict:
    out: dict = {}
    if "before" in value:
        import aws_sdk_ecs.types.timestamp

        out["before"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["before"]
        )
    if "after" in value:
        import aws_sdk_ecs.types.timestamp

        out["after"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["after"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatedAt:
    out: CreatedAt = {}  # type: ignore[typeddict-item]
    if "before" in data:
        import aws_sdk_ecs.types.timestamp

        out["before"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["before"]
        )
    if "after" in data:
        import aws_sdk_ecs.types.timestamp

        out["after"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["after"]
        )
    return out
